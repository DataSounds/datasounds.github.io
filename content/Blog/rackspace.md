Title: Now hosted at Rackspace Cloud
Date: 2013-07-22
Author: luizirber
status: draft

Our [oceansound demo][3] was running on a [Digital Ocean][9] droplet because
free PaaS alternatives weren't really viable. We extract timeseries from
MODIS data with an old version of PyHDF that still supports HDF4 and needed
about 4GB for data itself, so we deployed it and paid US$ 5/month.
It really wasn't expensive and performance was good, but we don't have any
income with this project so it would be better if we could avoid costs and
don't be restricted by our lack of infrastructure.

Not anymore.

Two weeks Jesse Noller [tweeted][4] that Rackspace was offering free cloud
accounts for OSS projects. Hmm. I sent him an email and he replied quickly,
offering us a new home.

After following his instructions and be amazed by [The Fanatical Support][8]
(first time someone called me right after sign up) last monday I started
the migration. When I deployed the demo to Digital Ocean I tried to avoid
as much as possible to do things by hand and [automated the process][6] with
[Ansible][5]. This time I adapted scripts to follow [best practices][7] and
started a security role, and everything went smoothly.

But the best part is that I have more resources available, and I set up a
[Jenkins builbot][1]. First test was to deploy this blog to [Cloud Files][10]
automatically, and I found a [tutorial][11] explaining how to make it work
as a static site. You're reading this, so it is working.

All in all, we are extremely satisfied with the experience, and we can't
recommend Rackspace enough. Great work!

[1]: http://ci.datasounds.org:8080/view/Build%20Pipeline/
[2]: http://www.datasounds.org
[3]: http://ocean.datasounds.org
[4]: https://twitter.com/jessenoller/status/355757374906183680
[5]: http://www.ansibleworks.com
[6]: https://github.com/DataSounds/oceansound_demo/tree/master/devops
[7]: http://www.ansibleworks.com/docs/bestpractices.html
[8]: http://www.rackspace.com/whyrackspace/support/
[9]: https://www.digitalocean.com
[10]: http://www.rackspace.com/cloud/files/
[11]: http://www.philipithomas.com/jekyll-on-cloud-files/
