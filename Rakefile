task :install do
  case
  when on?("darwin")
    puts "allow hjkl to repeat"
    sh "defaults write com.sublimetext.2 ApplePressAndHoldEnabled -bool false"

  when on?("linux")
    puts "copy command line binary"
    sh "sudo cp -v linux/subl /usr/bin/subl"

    puts "create and install .desktop"
    sh "sudo cp -v linux/sublime-text.desktop /usr/share/applications"
    sh "sudo cp -v linux/sublime-text.desktop /usr/share/gnome/app"
    sh "sudo cp -v linux/xampp_sublimetext2.png /usr/share/pixmaps"
  end

  puts "link user folder"
  sh "rm -rf #{sublime_dir}/Packages/User"
  sh "ln -s $HOME/sublime #{sublime_dir}/Packages/User"

  puts "provide shortcut"
  sh "ln -s #{sublime_dir} $HOME/.sublime.d"

  puts "get rid of existing js snippets"
  sh "rm #{sublime_dir}/Packages/JavaScript/*.sublime-snippet"
end

task :link, :proj do |t, args|
  proj = "~/#{args[:proj]}"
  target = "#{sublime_dir}/Packages/#{args[:proj]}"

  sh "rm -rf #{target}"
  sh "ln -s #{proj} #{target}"

  puts "linked #{proj} to #{target}"
end

task :unlink, :proj do |t, args|
  target = "#{sublime_dir}/Packages/#{args[:proj]}"

  sh "rm #{target}"

  puts "removed #{target}"
end

def sublime_dir
  case
  when on?("darwin") then "$HOME/Library/Application\\ Support/Sublime\\ Text\\ 2"
  end
end

def on?(platform)
  RUBY_PLATFORM.downcase.include?(platform)
end
