{% comment %}
As a maintainer, you don't need to edit this file.
If you notice that something doesn't work, please
open an issue: https://github.com/carpentries/styles/issues/new
{% endcomment %}

{% include manual_episode_order.html %}

<style>
  h2 {text-align: center;}
  #module-search {
    width: 100%;
    max-width: 600px;
    margin: 20px auto;
    padding: 12px 20px;
    font-size: 16px;
    border: 2px solid #ddd;
    border-radius: 4px;
    display: block;
  }
  #module-search:focus {
    outline: none;
    border-color: #4CAF50;
  }
  .search-container {
    text-align: center;
    margin-bottom: 20px;
  }
</style>

<div class="search-container">
  <input type="text" id="module-search" placeholder="Search modules by title or tags...">
</div>

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
<div class="row" id="modules-container">

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

<div class="col-6 col-sm-4 col-md-3 col-lg-2 col-xl-1 module-card" 
     data-title="{{ title_prefix}}{{ e.title | downcase }}" 
     data-tags="{{ tags | join: ' ' | downcase }}"
     data-url="{{ e.url | relative_url }}">
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

<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('module-search');
  const moduleCards = document.querySelectorAll('.module-card');
  const contentCache = {};

  // Fetch module content
  async function fetchModuleContent(url) {
    if (contentCache[url]) {
      return contentCache[url];
    }
    
    try {
      const response = await fetch(url);
      const html = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const content = doc.body.textContent.toLowerCase();
      contentCache[url] = content;
      return content;
    } catch (error) {
      console.error('Error fetching module content:', error);
      return '';
    }
  }

  searchInput.addEventListener('input', async function() {
    const searchTerm = this.value.toLowerCase().trim();

    if (searchTerm === '') {
      moduleCards.forEach(card => card.style.display = '');
      return;
    }

    for (const card of moduleCards) {
      const title = card.getAttribute('data-title');
      const tags = card.getAttribute('data-tags');
      const url = card.getAttribute('data-url');
      
      // First check title and tags for quick filtering
      const quickSearch = title + ' ' + tags;
      
      if (quickSearch.includes(searchTerm)) {
        card.style.display = '';
      } else {
        // If not found in title/tags, search the content
        const content = await fetchModuleContent(url);
        if (content.includes(searchTerm)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      }
    }
  });
});
</script>
