#!/usr/bin/env ruby
log_string = ARGV[0]
from = log_string.match(/\bfrom:([^\s\]]+)/)[1]
to = log_string.match(/\bto:([^\s\]]+)/)[1]
flags = log_string.match(/\bflags:([^\s\]]+)/)[1]

puts "#{from},#{to},#{flags}"
