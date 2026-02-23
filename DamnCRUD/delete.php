<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("location: login.php");
    exit();
} else {
    include 'functions.php';
    $pdo = pdo_connect();

    if (isset($_GET['id'])) {
        $stmt = $pdo->prepare('DELETE FROM contacts WHERE id = ?');
        $stmt->execute([$_GET['id']]);
        header("location:index.php");
        exit();
    } else {
        die ('No ID specified!');
    }
} 
?>