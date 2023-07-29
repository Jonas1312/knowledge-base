# GitHub

## Get PR diff or patch

Add .patch or .diff after url:

- <https://github.com/pytorch/pytorch/pull/20853.diff>
- <https://github.com/pytorch/pytorch/pull/20853.patch>

## GitHub Actions

### Tips

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

### Tools

- <https://www.actionsbyexample.com/>
- <https://marketplace.visualstudio.com/items?itemName=cschleiden.vscode-github-actions>
- <https://github-actions-hero.vercel.app/>
- <https://github.com/rhysd/actionlint>

## GitHub README Profile

<https://towardsdatascience.com/enrich-your-github-profile-with-these-tips-272fa1eafe05>

## Diagrams

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams>
