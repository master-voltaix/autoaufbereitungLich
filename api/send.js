// Vercel-Funktion: nimmt Anfragen aus dem Website-Formular entgegen und leitet sie per Resend weiter.
// Benötigte Umgebungsvariablen in Vercel (Settings → Environment Variables):
//   RESEND_API_KEY   API-Key aus Resend
//   MAIL_TO          Empfänger, z. B. autopflegeservice@online.de
//   MAIL_FROM        Absender mit in Resend verifizierter Domain, z. B. "Autopflege Leichlingen Website <anfrage@ihre-domain.de>"

const clean = (v, max) => String(v ?? '').replace(/[\r\0]/g, '').trim().slice(0, max);
const oneLine = (v, max) => clean(v, max).replace(/\n/g, ' ');
const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

module.exports = async (req, res) => {
  const wantsJson = req.headers['x-requested-with'] === 'fetch';
  const done = (ok) => {
    if (wantsJson) return res.status(ok ? 200 : 400).json({ ok });
    res.writeHead(303, { Location: ok ? '/danke.html' : '/kontakt.html' });
    return res.end();
  };

  if (req.method !== 'POST') return done(false);

  const { RESEND_API_KEY, MAIL_TO, MAIL_FROM } = process.env;
  if (!RESEND_API_KEY || !MAIL_TO || !MAIL_FROM) {
    console.error('send: Umgebungsvariablen fehlen');
    return done(false);
  }

  const b = req.body || {};
  if (clean(b.website, 100)) return done(true); // Honeypot

  const name = oneLine(b.name, 120);
  const telefon = oneLine(b.telefon, 60);
  const email = oneLine(b.email, 160);
  const leistung = oneLine(b.leistung, 120);
  const nachricht = clean(b.nachricht, 4000);
  const seite = oneLine(req.headers.referer, 300);

  if (!name || !telefon || !b.datenschutz) return done(false);
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return done(false);

  const rows = [
    ['Name', name],
    ['Telefon', telefon],
    ['E-Mail', email || '–'],
    ['Leistung', leistung || '–'],
  ];

  const text = 'Neue Anfrage über die Website\n\n'
    + rows.map(([k, v]) => `${k}: ${v}`).join('\n')
    + `\n\nNachricht:\n${nachricht || '–'}\n`
    + (seite ? `\nGesendet von: ${seite}\n` : '');

  const tel = telefon.replace(/[^0-9+]/g, '');
  const cell = (k, v) => {
    let val = esc(v);
    if (k === 'Telefon' && tel) val = `<a href="tel:${esc(tel)}">${val}</a>`;
    if (k === 'E-Mail' && email) val = `<a href="mailto:${esc(email)}">${val}</a>`;
    return `<tr><td style="border-bottom:1px solid #e1e5eb;color:#6b7686;width:110px">${k}</td>`
      + `<td style="border-bottom:1px solid #e1e5eb;font-weight:bold">${val}</td></tr>`;
  };
  const html = '<div style="font-family:Arial,sans-serif;font-size:15px;color:#131c2b;max-width:560px">'
    + '<h2 style="margin:0 0 16px;color:#10305c">Neue Anfrage über die Website</h2>'
    + `<table cellpadding="8" style="border-collapse:collapse;width:100%">${rows.map(([k, v]) => cell(k, v)).join('')}</table>`
    + '<p style="margin:20px 0 6px;color:#6b7686">Nachricht</p>'
    + `<p style="margin:0;white-space:pre-wrap">${nachricht ? esc(nachricht) : '–'}</p>`
    + (seite ? `<p style="margin:24px 0 0;font-size:12px;color:#6b7686">Gesendet von: ${esc(seite)}</p>` : '')
    + '</div>';

  const mail = {
    from: MAIL_FROM,
    to: MAIL_TO.split(',').map((s) => s.trim()),
    subject: `Neue Anfrage: ${leistung || 'Website'} – ${name}`,
    text,
    html,
  };
  if (email) mail.reply_to = email;

  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(mail),
    });
    if (!r.ok) console.error('send: Resend-Fehler', r.status, await r.text());
    return done(r.ok);
  } catch (err) {
    console.error('send: Resend nicht erreichbar', err);
    return done(false);
  }
};
