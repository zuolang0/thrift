<?php
namespace langzi;
error_reporting(E_ALL);
require_once __DIR__ . '/Thrift/ClassLoader/ThriftClassLoader.php';
use Thrift\ClassLoader\ThriftClassLoader;

$GEN_DIR = realpath(__DIR__.'/gen-php');
$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', __DIR__);
$loader->registerDefinition('langzi', $GEN_DIR);
$loader->register();
if (php_sapi_name() == 'cli') {
  ini_set("display_errors", "stderr");
}

#use Thrift\Protocol\TBinaryProtocol;
use Thrift\Protocol\TCompactProtocol;
use Thrift\Transport\TPhpStream;
use Thrift\Transport\TBufferedTransport;
use Thrift\TMultiplexedProcessor;

class upNameHandler implements \langzi\upNameIf {
    public function EditName($id, $name){
        return $name.'123';
    }
};
class upAddressHandler implements \langzi\upAddressIf {
    public function EditAddress($id, $address){
        return $address.'123';
    }
};
class upPwdHandler implements \langzi\upPwdIf {
    public function EditPassword($id, $pwd){
        return $pwd.'123';
    }
};
header('Content-Type', 'application/x-thrift');
if (php_sapi_name() == 'cli') {
  echo "\r\n";
}

$transport = new TBufferedTransport(new TPhpStream(TPhpStream::MODE_R | TPhpStream::MODE_W));
$protocol = new TCompactProtocol($transport, true, true);
$tMultiplexedProcessor = new TMultiplexedProcessor();

$handler = new upNameHandler();
$upNameProcessor = new upNameProcessor($handler);
$tMultiplexedProcessor->registerProcessor("upName", $upNameProcessor);

$upAddress = new upAddressHandler();
$upAddressProcessor = new upAddressProcessor($upAddress);
$tMultiplexedProcessor->registerProcessor("upAddress", $upAddressProcessor);

$upPwd = new upPwdHandler();
$upPwdProcessor = new upPwdProcessor($upPwd);
$tMultiplexedProcessor->registerProcessor("upPwd", $upPwdProcessor);
$transport->open();
$tMultiplexedProcessor->process($protocol, $protocol);
$transport->close();