<?php
$servername = "enter your ENDPOINT";
$database = "studentXdb";
$username = "admin";
$password = "enter master password";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}
  echo "<h1>Great!</h1><br>Connected successfully to:<b> $servername</b>";
?>