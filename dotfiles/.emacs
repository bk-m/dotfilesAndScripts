(prefer-coding-system 'utf-8)

(require 'package)

;; (setq package-list '(powerline zenburn-theme))
(setq package-list '(helm neotree flycheck spaceline))

(add-to-list 'package-archives
  '("melpa" . "http://melpa.org/packages/"))

(package-initialize)

; fetch the list of packages available 
(unless package-archive-contents
  (package-refresh-contents))

; install the missing packages
(dolist (package package-list)
  (unless (package-installed-p package)
    (package-install package)))

(toggle-frame-fullscreen)
(tool-bar-mode 0)
(menu-bar-mode 0)
(scroll-bar-mode 0)
(setq inhibit-startup-message t)
(setq initial-scratch-message
";;                                   _____       _    
;;  ___  _ __ __ _ _ __   __ _  ___  \\_   \\_ __ | | __
;; / _ \\| '__/ _` | '_ \\ / _` |/ _ \\  / /\\/ '_ \\| |/ /
;;| (_) | | | (_| | | | | (_| |  __/\\/ /_ | | | |   < 
;; \\___/|_|  \\__,_|_| |_|\\__, |\\___\\____/ |_| |_|_|\\_\\ 
;;                       |___/     emacs config

")

;; (custom-enabled-themes (quote (zenburn)))
(global-linum-mode t)
(setq linum-format "%d ")
;; (global-visual-line-mode t)
;; (line-number-mode t)
 
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Droid Sans Mono" :foundry "outline" :slant normal :weight normal :height 140 :width normal)))))

(global-set-key (kbd "C-?") 'help-command)
(global-set-key (kbd "M-?") 'mark-paragraph)
(global-set-key (kbd "C-h") 'delete-backward-char)
(global-set-key (kbd "M-h") 'backward-kill-word)
(global-set-key (kbd "M-x") 'helm-M-x)
(global-set-key (kbd "C-x C-b") 'helm-buffers-list)
(global-set-key [f8] 'neotree-toggle)

(setq helm-M-x-fuzzy-match t
 helm-mode-fuzzy-match t
 helm-buffers-fuzzy-matching t
 helm-recentf-fuzzy-match t
 helm-locate-fuzzy-match t
 helm-semantic-fuzzy-match t
 helm-imenu-fuzzy-match t
 helm-completion-in-region-fuzzy-match t
 helm-candidate-number-list 80
 helm-split-window-in-side-p t
 helm-move-to-line-cycle-in-source t
 helm-echo-input-in-header-line t
 helm-autoresize-max-height 0
 helm-autoresize-min-height 20)
(helm-mode 1)

(global-flycheck-mode)
(spaceline-emacs-theme)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (neotree helm))))
