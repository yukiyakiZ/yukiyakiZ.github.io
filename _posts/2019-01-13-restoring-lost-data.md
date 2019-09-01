---
layout: post
title: "Restoring Lost Data"
excerpt: ""
categories: [technical tips]
comments: true
---

<p class="lead text-justify">
    I never expected it to happen: I lost ALL the TeX files of my project documents when I accidentally
    clean up the codes and data on the git repository.
      It was indeed a nightmare since I had to reproduce the tedious tex formulas, figures and so forth.
    Fortunately, I finally obtained a rough recovery of the original documents.
    Below are the tips I learned.
</p>

<h4>Develop a Backup Strategy for Important Documents</h4>
<p class="lead text-justify">
    One would never emphasize the importance of data backup too much.
    Try to <font class="font-italic">prevent</font> the situation  of losing important data from happening with a custom backup strategy.
      One has to identify the potential risks, the aggregate size of target files, and concerns (e.g., privacy) before determining a proper backup method for best trade-offs.
  </p>
  <p class="lead text-justify">
      For me, I typically backup only the code base, TeX files, and pdf, which do not require a large space.
      The main risks for me are the potential to lose the personal laptop and the unintentional deletion of the files.
      I don't care about the privacy issues for my backup files.
    Hence, I typically backup important documents at cloud storage, e.g., private GitHub repo (which is now
      <a href="https://github.com/pricing">FREE</a> for all users)
    and synchronize it whenever significant changes are made.
    Such a method would make sure there is a copy at the remote GitHub server even if the personal laptop was lost.
      Meanwhile, I would be able to trace back to the previous commit even if I accidentally <code>rm -rf</code> the data.
      It strikes a proper balance between the convenience/cost and the risks for me.
  </p>
<p class="lead text-justify">
    I tried previously using the portable storage device to back up the data, however,
    I gave the burden up since I found it both time-consuming (full-backup) and not necessary due to the low utilization of >100GB storage space.
    For Mac OS users, TimeMachine could be an elegant/fancy option as well, which requires a NAS equipped Wi-Fi router called <a href="https://en.wikipedia.org/wiki/AirPort_Time_Capsule">AirPort Time Capsule</a>.
</p>

<h4>If It Unfortunately Happens ...</h4>
For me, I could not restore the data since I cleaned up the <code>.git</code> folder which encodes the history,
otherwise, I would simply `git reset --hard <HASH ID>` to help.

  <p class="lead text-justify">
    In desperate, I realized that I could probably get the data back by scanning the hardware disk.
    Fortunately (chances to recover depends on if the  <a href="http://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf">disk scheduler</a>
    overwrites the space of lost files,
    which is probabilistic and less likely as the time proceeds),
    I obtained the main lost files via the <a href="https://www.cleverfiles.com/help/">Disk Drill</a> application.
      Note that for MacOS 10.13+, in order to scan the hardware disk with a third party software,
      one has to turn off the file system protection temporarily via
      <code>csrutil disable</code> command at the terminal of the <a href="https://support.apple.com/en-us/HT201314">MacOS recovery mode</a>.
      Btw, to express the attitude for the data rescue, I paid and upgraded Disk Drill to PRO version :)
</p>
