---
layout: post
title: "Cheat Sheet of Using Clusters"
excerpt: ""
categories: [technical tips]
comments: true
---

I summarized the notes below of using ETH Zurich clusters (<a href="https://scicomp.ethz.ch/wiki/Euler">Euler</a>,
<a href="https://scicomp.ethz.ch/wiki/Leonhard">Leonhard</a>) based on the collected online tutorials
for a quick reference.

#### Accessing the compute node
Typically users could only see and interact with the login node as the gateway to the cluster black box.
However, upon the job run, one could use <code>bjob_connect jobID</code> command to monitor relevant information related to the compute node.

#### Checking the user profile
<code>busers</code> command could print out the user specifications, e.g., maximal jobs allowed to run.
Below is the print out of my expired student account.

{% highlight bash %}
[liayu@lo-login-02 ~]$ busers -w
USER/GROUP          JL/P    MAX  NJOBS   PEND    RUN  SSUSP  USUSP    RSV  MPEND  PJOBS MPJOBS   PRIO
liayu                  -   2400      0      0      0      0      0      0      -      0  25000      0
{% endhighlight %}

#### Job submission
Every job has to be submitted and handled by the batch system (Platform Load Sharing Facility/LSF) with respect to its
<a href="https://www.ibm.com/support/knowledgecenter/en/SSETD4_9.1.2/lsf_foundations/job_scheduling_dispatch_lsf.html">scheduling policy</a>.
<code>bsub [optional flags] < tmp.sh</code> will submit a job specified by the shell script.
One could specify the resource profile for the job, detailed bsub flags related to resource requests could be found
<a href="https://scicomp.ethz.ch/wiki/LSF_mini_reference">here</a>.

{% highlight bash %}
bsub -n 4 -W 120:00 -R "rusage[mem=10000]" "python3 x.py -y z
{% endhighlight %}

#### Interacting with a GitHub repo
Both HTTP or SSH could be leveraged, however, HTTP requires typing in your username and password when cloning or making pull/push requests
(but one could use <code>git config credential.helper 'cache --timeout=3600'</code> to cache the
password and ID for the avoidance).
With SSH, one could generate a RSA key pair via <code>ssh-keygen -t rsa</code> locally and provide an optional
passphrase for the two-factor authentication (what you know + what you have).
Then add the public key
stored in <code>~/.ssh/id_rsa.pub</code> to the GitHub <code>Settings/SSH and GPG keys</code>.
One could then simply type in the passphrase to interact with the GitHub repos conveniently,
e.g., <code>git clone git@github.com:{UserName}/{RepoName}.git</code>.

#### Handling signals
It is frustrating if the long-running jobs are killed without any logs saved
when they exceed the time limits originally requested.
LSF tries to terminate the job gradually by sending increasingly "unfriendly" signals:
USR2 when close to expiry => INT, QUIT, TERM and KILL after a grace period
=> brutal termination operation that can not be caught or ignored.
Hence, it is better to always handle the USR2 signal with a logging operation.
One could extend the grace period via <code>-ta USR2 -wt [hh:]mm</code> bsub arguments.

#### Job chaining
Job chaining is useful to split a long-running job into smaller units that fit into the time limits.
For example, I am only allowed to schedule a job <24h at Leonhard cluster.
<code>bsub -w (wait)</code> could specify the dependency over the previous job. E.g.,
the command below (submitted at once) states that
job2 will be executed only if job1 is done successfully, otherwise it will be cleared out automatically.
<code>ended(job1)</code> is the antonym of <code>done(job1)</code>, which states that job2 will be always executed.
<div class="p-3 lead mb-2 bg-light text-dark">
<pre>bsub -J job1 command1
bsub -J job2 -w "done(job1)" command2</pre></div>
The same program with a large number of <font class="font-italic">dependent</font> iterations could be split
as well, however, it requires
the programmer to decouple the pipeline of execution and input/output so that the new instance
of execution could base itself on the previous output.
One could chain the execution as well (giving the same name for the jobs is optional):
<pre>bsub -J long_job command
bsub -J long_job -w "done(long_job)" command
bsub -J long_job -w "done(long_job)" command</pre>
If one kills an intermediate job, it will exert a
<a ref="https://scicomp.ethz.ch/wiki/FAQ">domino effect</a>.

#### Status monitoring
<code>bjobs -p</code> will list all the pending jobs and <code>bjobs -p JOBID</code>
will list the detailed reason. <code>bbjobs JOBID</code> will give more detailed information on requested resources and so forth.
<code>bpeek JOBID</code> or <code>bpeek -J JOBNAME</code> will monitor the output real-time.
One could conveniently monitor the total number of jobs pending and running via
<code>bjobs | wc -l</code>.
Below is the finite state machine figure for the job status from the <a href="https://www.ibm.com/support/knowledgecenter/en/SSETD4_9.1.3/lsf_admin/job_state_lsf.html">IBM tutorial</a>.
<figure class="figure">
<img src="/img/BatchJobFSM.png" width="500" height="300" class="figure-img img-fluid rounded" alt="LSF">
    <figcaption class="figure-caption text-right"></figcaption>
</figure>

#### Killing jobs
<code>bkill JOBID</code> or <code>bkill -J jobname</code> will kill a specific job.
<code>bkill 0</code> will kill all pending and running jobs.
One could "kill" the job by sending a signal,
e.g., if there is a USR2 signal handler in the program, one could run
<code>bkill -s USR2 JOBID</code> to trigger the callback (e.g., logging) of the USR2 handler.


