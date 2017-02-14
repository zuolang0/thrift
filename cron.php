<?php
namespace Model;
error_reporting(E_ERROR | E_WARNING | E_PARSE);
set_time_limit(0);
date_default_timezone_set('Asia/Shanghai');
spl_autoload_register(function ($class) {
    echo $file = 'Model\\' .$class . '.class.php';
    if (is_file($file))
    {
        require_once $file;
    }

});
?>