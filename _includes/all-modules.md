{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include manual_episode_order.html %}

<style>
  h2 {text-align: center;}
</style>

<h3> </h3>

<div class="container-fluid">
<div class="row">

{% for lesson_episode in lesson_episodes %}

{% if site.module_order %}
  {% assign e = site.modules | where: "slug", lesson_episode | first %}
{% else %}
  {% assign e = lesson_episode %}
{% endif %}

{% assign title = e.title %}
{% if e.tags contains "scripting" %}
  {% assign title = "Scripting: " | append: title %}
{% endif %}
{% if e.tags contains "workflow" %}
  {% assign title = "Workflow: " | append: title %}
{% endif %}
{% if e.tags contains "draft" %}
  {% assign title = "(Draft) " | append: title %}
{% endif %}

{% assign tags = "" | split: ", " %}
{% for tag in e.tags %}
  {% unless tag == "scripting" or tag == "draft" or tag == "workflow" %}
    {% assign tags = tags | push: tag %}
  {% endunless %}
{% endfor %}


<div class="col-xs-4">
  <div class="panel panel-default">
    <div class="panel-heading">
      <a href="{{ e.url | relative_url }}">
        <h4>{{ title }}</h4>
        <h5>{{ tags | array_to_sentence_string: ',' }}</h5>
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
