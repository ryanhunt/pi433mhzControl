<?php

$secret = 'vypAoj8dgusfoTA9aJHw';

$file = '/tmp/ggggggg.txt';

$fp = fopen($file, 'w');
fwrite($fp, print_r($_POST, TRUE));
fwrite($fp, print_r($_BODY, TRUE));
fclose($fp);

?>
