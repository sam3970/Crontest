#!/usr/bin/perl

use strict;
use warnings;

my @queue_arr;
my @input = ('1','2','3');

foreach my $temp (@input)
{
	unshift(@queue_arr,$temp);
	print "push queue value $temp \n";
	print "add item to queue : @queue_arr \n";
}

print "---------------------------------------\n"; 
print "Stack : @queue_arr \n"; 
print "---------------------------------------\n";

my $count=@queue_arr;

foreach (1..$count)
{
	my $queue_pop = pop @queue_arr;
	print "stack pop value result is $queue_pop \n";
}

print "---------------------------------------\n"; 
print "Stack : @queue_arr \n"; 
print "---------------------------------------\n";

