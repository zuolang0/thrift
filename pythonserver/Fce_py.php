<?php
namespace langzi;
error_reporting(E_ALL);
require_once  './../Thrift/ClassLoader/ThriftClassLoader.php';

use Thrift\ClassLoader\ThriftClassLoader;

$GEN_DIR = realpath('./../gen-php');

$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', './../');
$loader->registerDefinition('langzi', $GEN_DIR);
$loader->register();

use Thrift\Protocol\TBinaryProtocol;
use Thrift\Protocol\TMultiplexedProtocol;
use Thrift\Transport\THttpClient;
use Thrift\Transport\TSocket;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;
use langzi\upNameClient;
use langzi\upAddressClient;
use langzi\EditPassword;




try {

/*  $socket = new THttpClient('localhost', 9090, '/Fse.php');
  $transport = new TBufferedTransport($socket);
  $protocol = new TBinaryProtocol($transport);*/

  #如果是Tsocket 则没有那个TBufferedTransport
  $transport = new  TSocket('localhost', 9099);
  $transport->open();
  $protocol = new TBinaryProtocol($transport);

#如果服务端使用TMultiplexedProcessor接收处理，客户端必须用TMultiplexedProtocol并且指定serviceName和服务端的一致
  $upNameProtocol = new TMultiplexedProtocol($protocol, 'upname');
  $upAddressProtocol = new TMultiplexedProtocol($protocol, 'upaddress');
  $upPwdProtocol = new TMultiplexedProtocol($protocol, 'uppwd');
#var_dump( $upNameProtocol);die;
  $upName = new upNameClient($upNameProtocol);
  $upAddress = new upAddressClient($upAddressProtocol);
  $upPwd = new upPwdClient($upPwdProtocol);


  $member = $upName->EditName(1, 'zl123');
  var_dump($member);

  $member = $upAddress->EditAddress(12, 'ld123');
  var_dump($member);

  $member = $upPwd->EditPassword(12, 'ld1231213');
  var_dump($member);
//   $transport->close();
} catch (TException $tx) {
  print 'TException: '.$tx->getMessage()."\n";
}