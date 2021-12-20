{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include manual_episode_order.html %}


<div class="container-fluid">
<div class="row">

{% for lesson_episode in lesson_episodes %}

{% if site.module_order %}
  {% assign e = site.modules | where: "slug", lesson_episode | first %}
{% else %}
  {% assign e = lesson_episode %}
{% endif %}

<div class="col-xs-6">
  <div style="border:1px solid white; margin: 20px; padding: 20px;">
    <a href="{{ e.url | relative_url }}">
      <h4>{{ e.title }}</h4>
    </a>
    <img src="{{ e.figure | relative_url }}" alt="">
  </div>
</div>  

{% endfor %}

</div>
</div>