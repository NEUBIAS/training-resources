{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include image_data_formats_course_order.html %}

<style>
  h2 {text-align: center;}
</style>
<h3> </h3>


{% for lesson_episode in lesson_episodes %}
{{ lesson_episode.title }}
{% endfor %}

{% assign episodes = "" | split:"," %}
{% for lesson_episode in lesson_episodes %}
{% if site.module_order %}
  {% assign e = site.modules | where: "slug", lesson_episode | first %}
{% else %}
  {% assign e = lesson_episode %}
{% endif %}
{% assign episodes = episodes | push: e %}
{% endfor %}


<div class="container-fluid">
<div class="row">

{% for e in episodes %}

{% assign tags = "" | split: ", " %}
{% for tag in e.tags %}
  {% unless tag == "scripting" or tag == "draft" or tag == "workflow" %}
    {% assign tags = tags | push: tag %}
  {% endunless %}
{% endfor %}

{% assign title_prefix = "" %}
{% if e.tags contains "draft" %}
  {% assign title_prefix = "Draft: " %}
{% elsif e.tags contains "workflow" %}
  {% assign title_prefix = "Workflow: " %}
{% elsif e.tags contains "scripting" %}
  {% assign title_prefix = "Scripting: " %}
{% endif %}

<div class="col-6 col-sm-4 col-md-3 col-lg-2 col-xl-1">
  <div class="panel panel-default">
    <div class="panel-heading">
      <a href="{{ e.url | relative_url }}">
        <h4>{{ title_prefix}}{{ e.title }}</h4>
        <!-- <h5>{{ tags | array_to_sentence_string }}</h5> -->
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
