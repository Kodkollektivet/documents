
(require 'package)

(add-to-list 'package-archives
             '("org" . "http://orgmode.org/elpa/") t)

(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents))

(defvar package-list
  '(org-plus-contrib))

(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      package-list)

(require 'ob-sql)
(require 'ob-sqlite)
(require 'org-drill)

(org-babel-do-load-languages
 'org-babel-load-languages
 '((emacs-lisp . t)
   (shell . t)
   (sql . t)
   (sqlite . t)
   (java . t)
   (python . t)))


(setq org-confirm-babel-evaluate nil)


(add-hook 'sql-interactive-mode-hook
          (lambda ()
            ('toggle-truncate-lines t)))


(setq org-src-window-setup 'current-window)
