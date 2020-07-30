#!/usr/bin/perl

#########################################
#developer : sklee02
#2020.03.28 : first time to develope
#2020.04.29 : modified to script syntax 
#########################################

use strict;
use warnings;
use utf8;
require teletime_pl;

binmode STDOUT, ":utf8";

#Global variable
#my $exTele = teletime_pl;


sub cron_test
{
    my $cron_value = qx(ps -ef |grep crond | grep -v grep | awk '{print \$8}' |sed -n 's|/usr/sbin/crond|crond|p');
	return $cron_value;
}

my $value = cron_test();
print $value;

#sms send part
if ($value =~ /^crond$/)
{
     #my $exTele=teletime_pl;
    my $msg="cron_test.pl 에서 테스트 통과!";
    my $exTele=teletime_pl::teleExpect($msg);
    printf ("프로세스가 정상적으로 실행중입니다.\n");
	#return $exTele;
}

else
{
    printf ("프로세스가 꺼져있어 작동을 재시작합니다.\n");
    system('service crond restart');
}

