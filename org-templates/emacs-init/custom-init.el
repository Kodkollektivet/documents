;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete these lines.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
(package-initialize)

;; load newest org-mode via cask install
;; for some reason it is necessary to load this before loading the configuration.org file
(add-to-list 'load-path "~/.emacs.d.kodkoll/.cask/25.1/elpa/org-plus-contrib-20170210")
     (require 'org-install)

;; custom org-mode configuration file
(org-babel-load-file "~/.emacs.d.kodkoll/configuration.org")
