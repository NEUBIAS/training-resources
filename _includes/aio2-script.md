{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include manual_episode_order.html %}

<style>
p.dotted {border-style: dotted;}
p.dashed {border-style: dashed;}
p.solid {border-style: solid;}
p.double {border-style: double;}
p.groove {border-style: groove;}
p.ridge {border-style: ridge;}
p.inset {border-style: inset;}
p.outset {border-style: outset;}
p.none {border-style: none;}
p.hidden {border-style: hidden;}
p.mix {border-style: dotted dashed solid double;}
</style>


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
    <a href="{{ e.url }}">
      <h4>{{ e.title }}</h4>
    </a>
    <img src="{{ e.figure }}" alt="">
  </div>
</div>  

{% endfor %}

</div>
</div>