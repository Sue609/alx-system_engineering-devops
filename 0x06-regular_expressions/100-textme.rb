#!/usr/bin/env ruby

log_file = ARGV[0]
File.open(log_file, 'r') do |file|
  file.each_line do |line|
    if line.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
      sender = $1
      receiver = $2
      flags = $3
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end
