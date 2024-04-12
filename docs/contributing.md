# Contributing to Vellox

Hello. Contributions to this project are highly encouraged and appreciated. This document will outline some general guidelines for how to get started.

## Contents

- [Creating a pull request](#creating-a-pull-request)
    * [Setting up the repository](#setting-up-the-repository)
- [Using the issue tracker](#using-the-issue-tracker)
    * [Technical support](#technical-support)
    * [Feature requests](#feature-requests)

## Creating a pull request

Non-trivial changes, especially those that could impact existing behaviour, should have an associated issue created for discussion. An issue isn't strictly required for larger changes, but it can be helpful to discuss first.

Minor changes generally should not require a new issue and can be explained in the pull request description.

### Setting up the repository

To create a pull request, you must first [fork](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-forks) the repository in GitHub, then clone the fork locally.

```shell
git clone git@github.com:<YOUR-USERNAME>/vellox.git
```

Then add the upstream remote to keep the forked repo in sync with the original.

```shell
cd vellox
git remote add upstream git://github.com/junah201/vellox.git
git fetch upstream
```

Then to keep in sync with changes in the primary repository, you pull the upstream changes into your local fork.

```shell
git pull upstream main
```

## Using the issue tracker

The issue [tracker](https://github.com/junah201/vellox/issues) can be used for different types of discussion, but it is mainly intended for items that are relevant to this project specifically.

Here are a few things you might consider before opening a new issue:

- Is this covered in the [documentation](https://vellox.junah.dev)?

- Is there already a related issue in the [tracker](https://github.com/junah201/vellox/issues)?

- Is this a problem related to Mangum itself or a third-party dependency?

It may still be perfectly valid to open an issue if one or more of these is true, but thinking about these questions might help reveal an existing answer sooner.

### Technical support

You may run into problems running Mangum that are related to a deployment tool (e.g. [Serverless Framework](https://www.serverless.com)), an ASGI framework (e.g. [FastAPI](https://fastapi.tiangolo.com/)), or some other external dependency. It is okay to use the tracker to resolve these kinds of issues, but keep in mind that this project does not guaruntee support for all the features of any specific ASGI framework or external tool.

**Note**: These issues will typlically be closed, but it is fine to continue discussion on a closed issue. These issues will be re-opened only if a problem is discovered in Vellox itself.

### Feature requests

This project is intended to be small and focused on providing an adapter class for ASGI applications deployed in [GCP Cloud Functions](https://cloud.google.com/functions). Feature requests related to this use-case will generally be considered, but larger features that increase the overall scope of Vellox are less likely to be included.

If you have a large feature request, please make an issue with sufficient detail and it can be discussed. Some feature requests may end up being rejected initially and re-considered later.

## Thank you

:)