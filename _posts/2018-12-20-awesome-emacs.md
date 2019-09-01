---
layout: post
title: "Awesome Emacs - A minimalistic collection of features"
excerpt: ""
categories: [technical tips]
comments: true
---

Spoiled by modern IDEs (and probably the absence of CS background during my undergraduate),
I originally treated text editors such as Emacs/Vim as a burden and simply used them reluctantly for terminals.
I started to seriously exploit Emacs
when I happened to witness during my internship how my mentor, a senior C programmer,
*live* in Emacs.
Especially, I was impressed when he fetched technical notes from his decades of experiences recorded by OrgMode, which precisely answered my question, in just several keyboard strokes before I realized it.

> I don't care what OS I use, it's just a boot loader for Emacs anyway. - Some U. Penn PhD student

Despite the Emacs steep learning curve, I was motivated  by OrgMode, the Emacs killer application, whenever I tried to give up.
            Fortunately, commands and interactions that appeared unintuitive at the beginning
            gradually made a lot more sense and I was fascinated by the unparalleled power of Emacs.
            I summarized a short list of Emacs features that benefited me most during my Emacs exploration.

### Note Taking
* *Org-drill:*
I used it to make flashcards (e.g., two-sided cards) with embedded spaced repetition algorithm to recap easy-to-forget knowledge in programming, German vocabulary and so on.
* *Org-capture:*
It provides an interface of template configuration to snapshot formatted information.
* *Tag management:*
One could set custom tags for the item via `C-c C-q` and search
targeted tags via `C-c a m` and
              <a href="https://orgmode.org/worg/org-tutorials/advanced-searching.html">proper syntax</a>.
* *Exporting:*
Emacs supports the compatible translation of org file to Latex, HTML and so forth.
One could write equations and formulas as if in tex files.

### GTD Workflow
Emacs is an excellent tool for task management.
I use <code>org-agenda</code> to manage TODO items and develop regular habits.
This <a href="https://blog.aaronbieber.com/2016/09/24/an-agenda-for-life-with-org-mode.html">tutorial</a> provides detailed steps to set up a personal agenda.

### Portable & Scalable Configuration
Emacs can be highly customized. When Emacs starts, it will consider <code>~/.emacs.d/init.el</code> config file
as the point of entry
<a href="https://www.gnu.org/software/emacs/manual/html_node/emacs/Init-File.html">by default</a>.
One could place all Emacs configurations under <code>~/.emacd.d</code> folder and back it up.
Emacs also allows scalable configuration.
For me, I prefer to use <code>~/.emacs.d/init.el</code> as the top layer to load <code>config.org</code> file
using <a href="https://orgmode.org/worg/org-contrib/babel/">org-babel</a> feature.
The benefit here is that one could combine the Emacs-lisp config code and OrgMode text to provide a self-explanatory configuration file.
    {% raw %}
    (defconst root-path "~/emacs.d/")
    (org-babel-load-file (concat root-path "config.org"))
    {% endraw %}

One could place the Emacs-Lisp code to be evaluated in <code>config.org</code>, which
then serves as a sub-layer to load my custom config modules classified by their functions.
    {% raw %}
    #+BEGIN_SRC emacs-lisp
    ((add-to-list 'load-path (concat root-path "modules/"))
    (require 'key-bindings)
    #+END_SRC
    {% endraw %}

Correspondingly, modules such as <code>~/.emacs.d/modules/key-bindings.el</code>
should end up with <code>(provide 'key-bindings)</code> declaration to enable the import.

### Custom Shortcuts and Variable Defaults
One could easily configure the favorable keyboard shortcuts to interact with Emacs.
E.g., provide shortcuts to Emacs function comment-region and uncomment-region instead of using
M-x to interactively trigger the function, which I found it inconvenient,

    {% raw %}
    (global-set-key "\C-x\M-c" 'comment-region)
    (global-set-key "\C-x\M-u" 'uncomment-region)
    {% endraw %}

To set \<f2\> as a shortcut to open Emacs <code>init.el</code> file, one has to define the function before attaching,
    {% raw %}
    (defun open-init-file()
        (interactive)
        (find-file "~/.emacs.d/init.el"))
    (global-set-key (kbd "&ltf2&gt") 'open-init-file)
    {% endraw %}

One could also configure the default variable values to modify the Emacs default behaviors.
E.g., to ask Emacs OrgMode to unfold all subsections,

    {% raw %}
    (setq org-startup-folded "showall")
    {% endraw %}

### A Nice Welcome Page
I prefer a simplistic default welcome page. Emacs allows us to configure it freely.

    {% raw %}
    ;; full screen by default
    (setq initial-frame-alist (quote ((fullscreen . maximized))))
    ;; remove startup screen
    (setq inhibit-startup-screen t)
    (setq inhibit-startup-message t)
    {% endraw %}

I also used <a href="https://github.com/narendraj9/quoted-scratch">quoted-scratch</a>
to pop my favorable saying in the start-up screen.

### Handy Preferences
Default Emacs UI interactions suffer me a lot.
I put a collection of minimal & comfortable settings
in <a href="https://github.com/liangcheng-yu/emacs.d/blob/master/modules/basic.el">GitHub repo</a>.

### Plethora of Possibilities
There is a spectrum of Emacs potentials with Emacs-Lisp Programming[^1].
I also use it (but less often) as a terminal (<code>M-x term</code>),
file system (<code>M-x dired</code>), 
platform to browse the website, read emails and so forth.

[^1]: [An Introduction to Programming in Emacs Lisp, Robert J. Chassell](https://www.gnu.org/software/emacs/manual/pdf/eintr.pdf)
