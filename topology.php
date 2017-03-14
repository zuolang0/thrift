<?php
error_reporting(E_ALL);
require_once __DIR__ . '/Thrift/ClassLoader/ThriftClassLoader.php';

use Thrift\ClassLoader\ThriftClassLoader;

$GEN_DIR = realpath(__DIR__.'/gen-php');

$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', __DIR__);
$loader->registerDefinition('topology', $GEN_DIR);
$loader->register();

if (php_sapi_name() == 'cli') {
    ini_set('display_errors', 'stderr');
}

use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TSocket;
use Thrift\Transport\THttpClient;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;

use topology\StormTopology;
use topology\NimbusClient;

#try{
    $socket = new THttpClient('192.168.70.168', 6627);
    $transport = new TBufferedTransport($socket, 1024,1024);
    $protocol = new TBinaryProtocol($transport);
    $client = new \topology\NimbusClient($protocol);

    $transport->open();
    $vals=array('spouts'=>array('RandomSentenceSpout()'),'bolts'=>array('SplitSentenceBolt()'));
    $topology=new \topology\StormTopology();
    $uploadedJarLocation='/usr/local/storm4/local/nimbus/inbox/stormjar-670f7548-d158-4826-8e39-bb6e0a419b35.jar';
    $name='testcount';
    $jsonConf=json_encode(array());
    $result=$client->submitTopology($name, $uploadedJarLocation, $jsonConf, $topology);

    echo $result;
    $transport->close();
#}catch (TException $e){
#    echo  'TException: '.$e->getMessage()."\n";
#}