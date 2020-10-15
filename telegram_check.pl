#!/usr/bin/perl

use strict;
use warnings;


sub telegramtest
{
    my $tele_value = qx(ps -ef | grep bin/telegram | grep -v grep | cut -c60-71);
    return $tele_value;
}

my $value = telegramtest();
print $value;


if ($value =~ "telegram_cli")
{
        printf ("success\n");
}
else
{
        printf ("fail\n");
}
