<?php

include 'secret.php';

if(isset($_POST['secret']) && (trim($_POST['secret']) != '') && trim($_POST['secret'] == $secret ) {
    $s=$_POST['secret'];
}
else {
    echo "Nope.";
    exit;
}

$file = '/tmp/ggggggg.txt';

$fp = fopen($file, 'w');
fwrite($fp, print_r($_POST, TRUE));
fwrite($fp, print_r($_BODY, TRUE));
fclose($fp);




?>
