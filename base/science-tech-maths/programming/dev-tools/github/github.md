# GitHub

## Get PR diff or patch

Add .patch or .diff after url:

- <https://github.com/pytorch/pytorch/pull/20853.diff>
- <https://github.com/pytorch/pytorch/pull/20853.patch>

## Release

Configuring automatically generated release notes: <https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes#configuring-automatically-generated-release-notes>

## GitHub Actions

### Matrix for multistage deployment

To roll out deployments for diff stages (staging, preprod, prod), you can use a matrix job that way:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        stage: [staging, preprod, prod]
        fail-fast: true  # stop all jobs if one fails
        max-parallel: 1  # run one job at a time
    steps:
      - name: Deploy
        run: |
          echo "Deploying to ${{ matrix.stage }}"
```

### Specifities of `push` event

A workflow can be triggered to run on a push event on certain branches:

```yaml
on:
  push:
    branches:
      - main
      - "release/**"
```

If the workflow is updated on the main branch, but not on the release branch, when you push on the release branch, the workflow will run with the old version of the workflow.

This happens since when a push event triggers the workflow, GitHub takes the commit SHA of the push event, and then looks for the workflow file at that commit SHA.

To always take the workflow from master while still using the on `push` event, one have to use the `uses` keyword to fetch the workflow from the main branch:

```yaml
on:
  push:
    branches:
      - main
      - "release/**"

jobs:
  my_job:
    runs-on: ubuntu-latest
    steps:
      - uses: {repo_owner}/{repo}/.github/workflows/{filename}@{ref}  # replace ref by main/master
```

### Env var

<https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables>

- `github.ref`: The branch or tag ref that triggered the workflow.
  - For workflows triggered by push, this is the branch or tag ref that was pushed.
  - For workflows triggered by pull_request, this is the pull request merge branch.
  - For workflows triggered by release, this is the release tag created.
  - For other triggers, this is the branch or tag ref that triggered the workflow run.
  - This is only set if a branch or tag is available for the event type.
  - The ref given is fully-formed, meaning that for branches the format is `refs/heads/<branch_name>`, for pull requests it is `refs/pull/<pr_number>/merge`, and for tags it is `refs/tags/<tag_name>`. For example, `refs/heads/feature-branch-1`.
- `github.ref_name`: The short ref name of the branch or tag that triggered the workflow run. This value matches the branch or tag name shown on GitHub. For example, `feature-branch-1`.

### Concurrency

Let's say you have a CI workflow that runs on every push to your PR branch. If you push 3 commits in a row, you'll end up with 3 concurrent workflows running at the same time. This can be a problem if you have a limited number of runners available, or if you're using a service that has a rate limit.

To avoid this, you can use the `concurrency` keyword to limit the number of concurrent workflows that can run on a given branch. For example, to limit the number of concurrent workflows to 1:

Example with concurrency at job level:

```yaml
on: [push]

jobs:
  pylint:
    runs-on: ubuntu-latest
    concurrency:
      group: ${{ github.workflow }}-pylint-${{ github.ref }}
      cancel-in-progress: true  # cancel any existing jobs in the group
    steps:
      ...
```

Example with concurrency at workflow level:

```yaml
on: [push]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # cancel any existing jobs in the group

jobs:
  pylint:
    runs-on: ubuntu-latest
    steps:
      ...
```

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref_name }}-${{ github.event.pull_request.number || github.sha }}
  cancel-in-progress: true
```

### Check if on tag

```yaml
if: startsWith(github.ref, 'refs/tags/')
```

### Tools

- <https://www.actionsbyexample.com/>
- <https://marketplace.visualstudio.com/items?itemName=cschleiden.vscode-github-actions>
- <https://github-actions-hero.vercel.app/>
- <https://github.com/rhysd/actionlint>
- <https://github.com/tj-actions/changed-files>

## GitHub README Profile

<https://towardsdatascience.com/enrich-your-github-profile-with-these-tips-272fa1eafe05>

## Diagrams

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams>
