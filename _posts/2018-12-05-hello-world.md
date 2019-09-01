---
layout: post
title: "Hello World Post - Plus tips to create an amateur website"
excerpt: "Custom written post descriptions are the way to go... if you're not lazy."
categories: [technical tips]
comments: true
# image:
#   feature: https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?crop=entropy&dpr=2&fit=crop&fm=jpg&h=475&ixjsv=2.1.0&ixlib=rb-0.3.5&q=50&w=1250
#   credit: Greg Rakozy
#   creditlink: https://unsplash.com/photos/oMpAz-DN-9I
---

Finally, I started to create my personal website and blog.
I found it worthwhile to commit myself to blogging and embrace the habit of being *persistent* during the trajectory.
Meanwhile, contents of the posts could also serve as long-term memory.

Trade-offs and decisions during the website creation can be highly personalized.
For me, the construction boils down to several aspects.

* *Server host:* <a href="https://pages.github.com">GitHub Pages</a> could be a good option
    for static websites which does most back-end configurations for you under the hood. However, one is not able to set up its own
    backend databases.
* *Domain name:*
One could register a custom domain name via DNS providers such as <a href="https://www.godaddy.com">GoDaddy</a>.
<code>CNAME</code> at the git repo must store the custom domain name.
<code>A</code> and <code>CNAME</code> record at the DNS provider should point to one of the GitHub's server IPs and corresponding `.github.io` domain name respectively.
<code>dig</code> command could be leveraged to confirm that the linking is taking effect (after variant DNS caching delay) as shown below. Note <code>192.30.252.153</code> could also work but will not enable HTTPS for the custom domain.
{% highlight bash %}
$ dig +noall +answer liangcheng-yu.github.io
liangcheng-yu.github.io. 3553	IN	A	185.199.108.153
liangcheng-yu.github.io. 3553	IN	A	185.199.111.153
liangcheng-yu.github.io. 3553	IN	A	185.199.110.153
liangcheng-yu.github.io. 3553	IN	A	185.199.109.153
$ dig +noall +answer liangchengyu.com
liangchengyu.com.	567	IN	A	185.199.108.153
{% endhighlight %}
*   *SNAPSHOT version:*
    As a beginner, mature front-end frameworks such as 
    [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) are helpful to set up a scratch theme.
    I personally prefer using a modular & simplistic (no meaningless icons, blocks, scrolls) [jekyll](https://jekyllrb.com) theme since it will allow me to write in markdown (also compatible with html) and edit efficiently in Vim. Besides, I found the jekyll's support for [Liquid templating language](https://shopify.github.io/liquid/basics/introduction/) to be extremely handy and save repetitive labour work.
* *Front-end customization:*
    I found it useful to reverse engineer the favorable web components during web surfing via inspecting the source code fetched by the browser client.

**Tips** The book [Design for Hackers: Reverse Engineering Beauty](https://www.amazon.com/Design-Hackers-Reverse-Engineering-Beauty/dp/1119998956) is  informative for ameteur web designers on topics of typography, geometric proportions, hierarchy of information, color theory, and most importantly, the mindset of reverse engineering the artifacts you see every day.
{: .notice}

* *Optimization:*
    Due to geographical reasons, access from China might suffer from severe delay. Registration at a local CDN provider could mitigate the issue.
    One could also perform SEO to the website, e.g., simply via <a href="https://help.github.com/articles/search-engine-optimization-for-github-pages/">Jekyll SEO tag plugin</a>.
* *Security:*
    One could easily enable HTTPS with <code>Settings</code> at GitHub repo and make sure the DNS record points to one of the HTTPS-active GitHub server IPs.
    One could also authenticate the website ownership via the asymmetric key mechanism provided by <a href="https://keybase.io">Keybase</a>.