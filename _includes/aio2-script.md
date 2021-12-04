{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include manual_episode_order.html %}


<div class="row">

{% for lesson_episode in lesson_episodes %}

{% if site.module_order %}
  {% assign e = site.modules | where: "slug", lesson_episode | first %}
{% else %}
  {% assign e = lesson_episode %}
{% endif %}

<div class="col-sm-6">
  <div class="card border-primary bg-dark" style="max-width: 24rem;">
    <div class="card-header">{{ e.title }}</div>
    <div class="card-body">
      <h5 class="card-title">Info card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    </div>
  </div>
</div>  

<hr />
{% endfor %}
</div>

{% comment %}
<div class="card-body">
      <img class="card-img-top" src="{{ e.figure }}" alt="Card image cap">
    </div>
{% endcomment %}