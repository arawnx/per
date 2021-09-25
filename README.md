# Dependencies
+ [pyyaml](https://github.com/yaml/pyyaml)

# Usage
`per [add|complete|...] [arg...]`

## Commands
`add title`

Creates a default item with name `title`.

`complete id`

Marks the item with id `id` as completed.

`delete id`

Deletes the item with id `id`.

`edit`

Opens `items.yaml` in vim for editing

`list|ls`

Lists all items

`inbox`

Filters and lists inbox items

`projects`

Filters and lists project names

`tickled`

Filters and lists items in the tickler

## Examples

`per add "My first item"` — Creates a new item with `title` "My first item;" presumably with ID 0.

`per e` — Opens `items.yaml` for editing. Uses shorthand: Most commands can be shortened.

`per complete 0` — Marks the item with `id` 0 as completed.

`per delete 0` — Deletes the item with `id` 0.