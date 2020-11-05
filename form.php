<?php
if(isset($_POST['submit'])) {
  $name = $_POST['name'];
  $password = $_POST['password'];
  $email = $_POST['email'];
  $age = $_POST['age'];
  $date = $_POST['date'];
  $number = $_POST['number'];
  $cell = $_POST['cell'];
  $genre = $_POST['genre'];
  $dropdown = $_POST['dropdown'];
  $text = $_POST['text'];
  $checkbox = $_POST['checkbox'];
  $gender = $_POST['gender'];
  $file = $_POST['file'];
  $url = $_POST['url'];
  $color = $_POST['color'];
  $hidden = $_POST['hidden'];

$host = "cdmga.com";
$dbUsername = "cdmgacom_form_project";
$dbPassword = "form_project";
$dbname = "cdmgacom_form_project";
$dbconnect = mysqli_connect($host, $dbUsername, $dbPassword, $dbname);
$sql =mysqli_query ($dbconnect, "insert into std_admission (ID, name, password, email, age, date, number, cell, genre, dropdown, text, checkbox, gender, file, url, color, hidden) values('', '$name', '$password', '$email', '$age', '$date', '$number', '$cell', '$genre' '$dropdown', '$text', '$checkbox', '$gender', '$file', '$url', '$color', '$hidden')");
if($sql) {
	echo "Data inserted successfully!";
	}
	else {
	echo "Failed to inser...";
  }
}
?>