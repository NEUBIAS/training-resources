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



{% assign all = episodes %}
{% assign workflows = episodes | where_exp: "item", "item.tags contains 'workflow'" %}
{% assign scriptings = episodes | where_exp: "item", "item.tags contains 'scripting'" %}
{% assign drafts = episodes | where_exp: "item", "item.tags contains 'draft'" %}



<div class="container-fluid">
<div class="row">
{% for e in all %}

{% if e.tags contains "draft" or e.tags contains "workflow" or e.tags contains "scripting" %}
{% continue %}
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
        <h4>{{ e.title }}</h4>
        <h5>{{ tags | array_to_sentence_string }}</h5>
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



<h2> Workflows </h2>
<div class="container-fluid">
<div class="row">
{% for e in workflows %}

{% if e.tags contains 'draft' %}
{% continue %}
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
        <h4>{{ e.title }}</h4>
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



<h2> Scripting </h2>
<div class="container-fluid">
<div class="row">
{% for e in scriptings %}

{% if e.tags contains "draft" %}
{% continue %}
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
        <h4>{{ e.title }}</h4>
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



<h2> Drafts </h2>
<div class="container-fluid">
<div class="row">
{% for e in drafts %}

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
        <h4>{{ e.title }}</h4>
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


