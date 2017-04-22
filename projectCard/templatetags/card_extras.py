from django import template
register = template.Library()

@register.filter
def group(groups, num):
	sequence = []
	for group in groups:
		if group.group == num:
			sequence.append(group)
	return sequence

