<?php
// Versand der Website-Anfragen per E-Mail. Benötigt PHP mit aktivierter mail()-Funktion beim Hoster.
$empfaenger = 'autopflegeservice@online.de';

$istFetch = isset($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'fetch';

function antwort($ok, $istFetch) {
    if ($istFetch) {
        header('Content-Type: application/json; charset=utf-8');
        if (!$ok) http_response_code(400);
        echo json_encode(['ok' => $ok]);
    } else {
        header('Location: ' . ($ok ? 'danke.html' : 'kontakt.html'));
    }
    exit;
}

function feld($name, $max) {
    $wert = isset($_POST[$name]) ? trim((string)$_POST[$name]) : '';
    $wert = str_replace(["\r", "\0"], '', $wert);
    return mb_substr($wert, 0, $max);
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') antwort(false, $istFetch);

// Honeypot: von Menschen nicht ausgefüllt
if (feld('website', 100) !== '') antwort(true, $istFetch);

$name      = str_replace("\n", ' ', feld('name', 120));
$telefon   = str_replace("\n", ' ', feld('telefon', 60));
$email     = str_replace("\n", '', feld('email', 160));
$leistung  = str_replace("\n", ' ', feld('leistung', 120));
$nachricht = feld('nachricht', 4000);

if ($name === '' || $telefon === '' || empty($_POST['datenschutz'])) antwort(false, $istFetch);
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) antwort(false, $istFetch);

$betreff = 'Anfrage über die Website' . ($leistung !== '' ? ': ' . $leistung : '');
$text = "Name: $name\nTelefon: $telefon\nE-Mail: " . ($email ?: '-') . "\nLeistung: " . ($leistung ?: '-') . "\n\n$nachricht\n";

$host = preg_replace('/[^a-z0-9.\-]/i', '', $_SERVER['SERVER_NAME'] ?? 'localhost');
$kopf = [
    'From: Website <noreply@' . $host . '>',
    'Content-Type: text/plain; charset=utf-8',
];
if ($email !== '') $kopf[] = 'Reply-To: ' . $email;

$ok = mail($empfaenger, '=?UTF-8?B?' . base64_encode($betreff) . '?=', $text, implode("\r\n", $kopf));
antwort($ok, $istFetch);
