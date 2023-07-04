#!/usr/bin/env ruby

log_file = ARGV[0]
File.open(log_file, 'r') do |file|
  file.each_line do |line|
    if line.match(/(\[from:.*?\]) (\[to:.*?\]) (\[flags:.*?\])/)
      sender = line.match(/(\[from:.*?\])/)[1].gsub(/\[from:|\]/, '')
      receiver = line.match(/(\[to:.*?\])/)[1].gsub(/\[to:|\]/, '')
      flags = line.match(/(\[flags:.*?\])/)[1].gsub(/\[flags:|\]/, '')
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end
