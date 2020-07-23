#!/usr/bin/perl

use strict;
use warnings;

my @stack_arr;
my @input = ('1','2','3');

foreach my $temp (@input)
{
	push(@stack_arr,$temp);
	print "add item to queue : @stack_arr \n"
}

print "---------------------------------------\n"; 
print "Stack : @stack_arr \n"; 
print "---------------------------------------\n";

my $count=@stack_arr;

foreach (1..$count)
{
	my $stack_pop = pop @stack_arr;
	print "stack pop value result is @stack_arr \n";
}

print "---------------------------------------\n"; 
print "Stack : @stack_arr \n"; 
print "---------------------------------------\n";

