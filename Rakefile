task :install do
  case
  when RUBY_PLATFORM.downcase.include?("darwin")
    sh "defaults write com.sublimetext.2 ApplePressAndHoldEnabled -bool false"
  when RUBY_PLATFORM.downcase.include?("linux")
    sh "sudo cp -v linux/subl /usr/bin/subl"
    sh "sudo cp -v linux/sublime-text.desktop /usr/share/applications"
    sh "sudo cp -v linux/sublime-text.desktop /usr/share/gnome/app"
    sh "sudo cp -v linux/xampp_sublimetext2.png /usr/share/pixmaps"
  end
end
