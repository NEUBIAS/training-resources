{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include manual_episode_order.html %}

<<<<<<< HEAD
=======
<style>
  h2 {text-align: center;}
</style>

<h2>Training Modules Overview</h2>
>>>>>>> master

<div class="container-fluid">
<div class="row">

{% for lesson_episode in lesson_episodes %}

{% if site.module_order %}
  {% assign e = site.modules | where: "slug", lesson_episode | first %}
{% else %}
  {% assign e = lesson_episode %}
{% endif %}

<div class="col-xs-6">
  <div class="panel panel-default">
    <div class="panel-heading">
      <a href="{{ e.url | relative_url }}">
        <h4>{{ e.title }}</h4>
      </a>
    </div>
    <div class="panel-body">
      <img src="{{ e.figure | relative_url }}" alt="">
    </div>
  </div>
</div>

{% endfor %}

</div>
</div>
