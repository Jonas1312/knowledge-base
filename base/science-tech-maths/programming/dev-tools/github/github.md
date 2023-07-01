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

### Tools

- <https://www.actionsbyexample.com/>
- <https://marketplace.visualstudio.com/items?itemName=cschleiden.vscode-github-actions>
- <https://github-actions-hero.vercel.app/>
- <https://github.com/rhysd/actionlint>

## GitHub README Profile

<https://towardsdatascience.com/enrich-your-github-profile-with-these-tips-272fa1eafe05>

## Diagrams

<https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams>
