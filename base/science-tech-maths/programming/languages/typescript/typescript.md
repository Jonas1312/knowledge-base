# Typescript

## NVM

Helps to manage multiple versions of Node

## Node

It is a JavaScript runtime built on Chrome's V8 JavaScript engine.

## NPM

It is a package manager for the JavaScript programming language. It is installed with Node.js.

It puts modules in place so that node can find them, and manages dependency conflicts intelligently.

Some windows specifics: <https://docs.npmjs.com/try-the-latest-stable-version-of-npm>

Useful commands:

```bash
npm install -g npm@latest  # update npm
```

When executables are installed via npm packages, npm creates links to them:

- local installs have links created at the `./node_modules/.bin/` directory
- global installs have links created from the global `bin/` directory (for example: `/usr/local/bin` on Linux or at `%AppData%/npm` on Windows)

To execute a package with npm you either have to type the local path, like this:

```bash
./node_modules/.bin/your-package
```

If  you want to run a package, you have to specify it in your package.json file.

```json
{
  "name": "your-application",
  "version": "1.0.0",
  "scripts": {
    "your-package": "your-package"
  }
}
```

Then you can run it with:

```bash
npm run your-package
```

Note that `npm test`, `npm start`, `npm restart`, and `npm stop` are all aliases for `npm run xxx`.

## NPX

It is a tool for executing Node packages. It is installed with Node.js.

It's a npm package runner that allows you to run any package from the npm registry without having to install it.

```bash
npx ts-node src/index.ts
```

## Typescript (TS)

It is a superset of JavaScript that compiles to plain JavaScript.

```bash
npm install -g typescript
```

## eslint

It is a tool for identifying and reporting on patterns found in ECMAScript/JavaScript code, with the goal of making code more consistent and avoiding bugs.

```bash
npm install -g eslint
```

## Var vs Let vs Const

- `var` declarations are globally scoped or function scoped while
- `let` and `const` are block scoped
- `var` variables can be updated and re-declared within its scope
- `let` variables can be updated but not re-declared
- `const` variables can neither be updated nor re-declared

## Equality

- `==` checks for value equality with coercion allowed. (i.e. `2 == '2'` is true)
- `===` checks for value equality without allowing coercion. (i.e. `2 === '2'` is false)

Similar to `==` vs. `===`, there is `!=` vs. `!==`

So ProTip: Always use `===` and `!==` to avoid type coercion.

### Scructures

If you want to compare two objects for structural equality ==/=== are not sufficient. e.g.

```ts
const a = { foo: 'bar' };
const b = { foo: 'bar' };
console.log(a === b); // false
```

To compare the two objects, you need to compare their properties:

```ts
const a = { foo: 'bar' };
const b = { foo: 'bar' };
console.log(a.foo === b.foo); // true
```

Or you can use a library like `deep-equal` or `lodash.isequal` to do the comparison for you.

## Null vs Undefined

- `undefined` means a variable has been declared but has not yet been assigned a value
- `null` is an assignment value. It can be assigned to a variable as a representation of no value

```ts
// Both null and undefined are only `==` to themselves and each other:
console.log(null == null); // true (of course)
console.log(undefined == undefined); // true (of course)
console.log(null == undefined); // true


// You don't have to worry about falsy values making through this check
console.log(0 == undefined); // false
console.log('' == undefined); // false
console.log(false == undefined); // false
```

To check if a var is `null` or `undefined`:

```ts
if (myVar == null) {
  // myVar is either null or undefined
}
```

### Json

`JSON.stringify` omits `undefined`` and function values when found in an object:

```ts
JSON.stringify({willStay: null, willBeGone: undefined}); // {"willStay":null}
```

## More


- <https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html>
- <https://exercism.org/tracks/typescript>
- <https://basarat.gitbook.io/typescript/getting-started/why-typescript>
- <https://github.com/gibbok/typescript-book>

<https://basarat.gitbook.io/typescript/future-javascript/arrow-functions>
<https://jsisweird.com/>
<https://medium.com/@PepsRyuu/use-let-by-default-not-const-58773e53db52>
<https://bun.sh/blog/bun-v1.0>
<https://www.devoreur2code.com/fr/blog/typescript-types-interfaces-and-classes>
<https://www.youtube.com/watch?v=i0YfiQlzv6M&list=PL9wyAJMCdd0mL9Vz-vzwPIp9U0hnCSWwe&index=18>
<https://github.com/type-challenges/type-challenges/>
