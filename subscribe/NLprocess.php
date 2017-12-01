<?php

// Hello! welcome to the settings page.
// Here's your two steps guide:

// FIRST: 
// Instead of newsletter@test.com put the email address of the mailing list,
// (the same that SendBlaster uses in Manage Subscriptions Section)
// ... please pay attention to the  ' ' apostrophes, they must remain around the email address.

$emailmanager = 'tingchunw@nvidia.com';

// SECOND:
// save this file, and close it. Thank you!


error_reporting(0);

$email = trim($_POST['email']);
$Ok = ereg("^([a-zA-Z0-9_\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$", $email);
if ($Ok) {
	mail($emailmanager,'Subscribe','','From: '.$email);

	if(!ereg("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$",$UNameFrm))
	{
	?>
<script language = 'javascript'>
	alert('Thank you, your address was added to our Mailing List');
	history.go(-1);
	</script>
<?
	exit();
	}
} 

else {
	if(!ereg("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$",$UNameFrm))
	{
	?>
<script language = 'javascript'>
	alert('Sorry, please provide a valid Email address.');
	history.go(-1);
	</script>
<?
	exit();
	}
}
?>
