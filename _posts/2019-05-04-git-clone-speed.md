---
layout: post
title: "Faster Git Clone Speed"
excerpt: ""
categories: [technical tips]
comments: true
---

It could be painful to `git clone` a large repo with a speed of 10-30 kbps.
Several tips to potentially boost the speed:

* Leverage VPN proxies, e.g., ShadowSocks
{% highlight bash %}
# Or edit ~/.gitconfig directly
git config --global http.proxy socks5://127.0.0.1:1086
git config --global https.proxy socks5://127.0.0.1:1086
{% endhighlight %}

* Avoid DNS pollution
{% highlight bash %}
# Add extra lines in /etc/hosts to circumvent DNS protocol
151.101.72.249	global-ssl.fastly.net
192.30.253.112  github.com
{% endhighlight %}

* Clone only the latest version
{% highlight bash %}
git clone --depth=1 https://github.com/x/y.git
{% endhighlight %}

* Increase buffer sizes
{% highlight bash %}
git config --global http.postBuffer 524288000
git config --global https.postBuffer 524288000
{% endhighlight %}

