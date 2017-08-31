# flake8: noqa

{% extends 'base.html' %}

{% load widget_tweaks %}

{% block content %}
  <form method="get">
    <div class="well">
      <h4 style="margin-top: 0">Filter</h4>
      <div class="row">
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.form.project.label_tag }}
          {% render_field filter.form.username class="form-control" %}
        </div>
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.form.approach.label_tag }}
          {% render_field filter.form.approach class="form-control" %}
        </div>
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.form.user.label_tag }}
          {% render_field filter.form.user class="form-control" %}
        </div>
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.form.database.label_tag }}
          {% render_field filter.form.database class="form-control" %}
        </div>
        <div class="form-group col-sm-8 col-md-6">
          {{ filter.form.sample.label_tag }}
          {% render_field filter.form.sample %}
          <div>
            {% for choice in filter.form.result %}
              <label class="checkbox-inline">
                {{ choice.tag }} {{ choice.choice_label }}
              </label>
            {% endfor %}
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">
        <span class="glyphicon glyphicon-search"></span> Search
      </button>
    </div>
  </form>

  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Project</th>
        <th>Approach</th>
        <th>Equipment</th>
        <th>Sample</th>
      </tr>
    </thead>
    <tbody>
      {% for user in filter.qs %}
        <tr>
          <td>{{ result.project }}</td>
          <td>{{ result.approach }}</td>
          <td>{{ result.equipment }}</td>
          <td>{{ result.sample }}</td>
          <td>
            {% for sample in result.sample.all %}
              {{ group }}
            {% empty %}
              <em class="text-muted">No matching sample were found.</em>
            {% endfor %}
          </td>
        </tr>
      {% empty %}
        <tr>
          <td colspan="5">No samples on the database</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
