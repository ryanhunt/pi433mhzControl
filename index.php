<?php

include 'secret.php';

/*

Array
(
    [secret] => ????
    [long] => 151.080645065506
    [lat] => -33.9834171320714
)

*/


if(isset($_POST['secret']) && (trim($_POST['secret']) != '') && (trim($_POST['secret']) == $secret) ) {
    $s=$_POST['secret'];
    echo "Yep.";
}
else {
    echo "Nope.";
    exit;
}


?>
