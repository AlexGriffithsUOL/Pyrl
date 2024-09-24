/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',
        // '../../../**/templates/**/*.html'
        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'pyrl-active': '#1a1ae8',
                'pyrl-light': '#5d5def',
                'pyrl-100': '#e8e8fd',
                'pyrl-200': '#b9b9f8',
                'pyrl-300': '#8b8bf3',
                'pyrl-400': '#5d5def',
                'pyrl-500': '#2e2eea',
                'pyrl-600': '#1515d1',
                'pyrl-700': '#1010a2',
                'pyrl-800': '#0c0c74',
                'pyrl-900': '#070746',

            },
            animation: {
                marquee: 'marquee 25s linear infinite',
                marquee2: 'marquee2 25s linear infinite',
                marquee3: 'marquee3 30s linear infinite',
            },
            keyframes: {
                marquee: {
                '0%': { transform: 'translateX(0%)' },
                '100%': { transform: 'translateX(-100%)' },
                },
                marquee2: {
                '0%': { transform: 'translateX(100%)' },
                '100%': { transform: 'translateX(0%)' },
                },
                marquee3: {
                '0%': { transform: 'translateX(0%)' },
                '100%': { transform: 'translateX(-100.65%)' },
                },
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}

// module.exports = {
//     extend: {
//         animation: {
//           marquee: 'marquee 25s linear infinite',
//           marquee2: 'marquee2 25s linear infinite',
//         },
//         keyframes: {
//           marquee: {
//             '0%': { transform: 'translateX(0%)' },
//             '100%': { transform: 'translateX(-100%)' },
//           },
//           marquee2: {
//             '0%': { transform: 'translateX(100%)' },
//             '100%': { transform: 'translateX(0%)' },
//           },
//         },
//     },
// }
