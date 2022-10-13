"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.findModule = exports.updateAngularJsonRule = exports.ngAdd = exports.addToModule = exports.getSourceFile = void 0;
const core_1 = require("@angular-devkit/core");
const schematics_1 = require("@angular-devkit/schematics");
const tasks_1 = require("@angular-devkit/schematics/tasks");
const change_1 = require("@schematics/angular/utility/change");
const find_module_1 = require("@schematics/angular/utility/find-module");
const ts = require("typescript");
const ast_utils_1 = require("./ast-utils");
/**
 * Reads file given path and returns TypeScript source file.
 */
function getSourceFile(host, path) {
    const buffer = host.read(path);
    if (!buffer) {
        throw new schematics_1.SchematicsException(`Could not find file for path: ${path}`);
    }
    const content = buffer.toString();
    const source = ts.createSourceFile(path, content, ts.ScriptTarget.Latest, true);
    return source;
}
exports.getSourceFile = getSourceFile;
/**
 * Import and add module to specific module path.
 */
function addToModule(host, modulePath, moduleName, src) {
    const moduleSource = getSourceFile(host, modulePath);
    const changes = (0, ast_utils_1.addImportToModule)(moduleSource, modulePath, moduleName, src);
    const recorder = host.beginUpdate(modulePath);
    changes.forEach((change) => {
        if (change instanceof change_1.InsertChange) {
            recorder.insertLeft(change.pos, change.toAdd);
        }
    });
    host.commitUpdate(recorder);
}
exports.addToModule = addToModule;
function ngAdd(options) {
    return (tree, context) => {
        let projectName = options.project;
        if (!projectName || projectName === '') {
            projectName = options.defaultProject;
        }
        options.path = 'app/example-pdf-viewer';
        options.name = 'example-pdf-viewer';
        options.skipImport = false;
        const stable = options.stable;
        const exampleComponent = options.exampleComponent;
        if (!projectName) {
            throw new schematics_1.SchematicsException("The project doesn't exist.");
        }
        context.addTask(new tasks_1.NodePackageInstallTask());
        if (exampleComponent) {
            const folder = projectName === options.defaultProject ? '/src' : `/projects/${projectName}/src`;
            const exampleComponentRule = generateExampleComponent(folder, stable);
            return (0, schematics_1.chain)([exampleComponentRule, updateAngularJsonRule(projectName, stable), addDeclarationToNgModule(options)]);
        }
        // return updateAngularJson(tree, projectName, stable);
        return tree;
    };
}
exports.ngAdd = ngAdd;
function updateAngularJsonRule(projectName, stable) {
    return (tree, _context) => {
        return updateAngularJson(tree, projectName, stable);
    };
}
exports.updateAngularJsonRule = updateAngularJsonRule;
function updateAngularJson(tree, projectName, stable) {
    const content = tree.read('./angular.json');
    const currentAngularJson = content.toString();
    const json = JSON.parse(currentAngularJson);
    if (!json['projects'][projectName]) {
        throw new schematics_1.SchematicsException("The project isn't listed in the angular.json.");
    }
    const optionsJson = json['projects'][projectName]['architect']['build']['options'];
    if (!stable) {
        optionsJson['assets'].push({
            glob: '**/*',
            input: 'node_modules/ngx-extended-pdf-viewer/bleeding-edge/',
            output: '/bleeding-edge/',
        });
    }
    else {
        optionsJson['assets'].push({
            glob: '**/*',
            input: 'node_modules/ngx-extended-pdf-viewer/assets/',
            output: '/assets/',
        });
    }
    json['projects'][projectName]['architect']['build']['options'] = optionsJson;
    const updatedAngularJson = JSON.stringify(json, null, 2);
    tree.overwrite('./angular.json', updatedAngularJson);
    return tree;
}
function generateExampleComponent(folder, stable) {
    const templateSource = (0, schematics_1.apply)((0, schematics_1.url)('./files'), [
        (0, schematics_1.applyTemplates)({
            classify: core_1.strings.classify,
            dasherize: core_1.strings.dasherize,
            stable: stable,
        }),
        (0, schematics_1.move)((0, core_1.normalize)(folder)),
    ]);
    return (0, schematics_1.chain)([(0, schematics_1.mergeWith)(templateSource)]);
}
function addDeclarationToNgModule(options) {
    return (host) => {
        if (options.skipImport || !options.module) {
            options.module = findModule(host, 'src/app/pdf-viewer');
            if (!options.module) {
                return host;
            }
        }
        const modulePath = options.module;
        const text = host.read(modulePath);
        if (text === null) {
            throw new schematics_1.SchematicsException(`File ${modulePath} does not exist.`);
        }
        const sourceText = text.toString('utf-8');
        const source = ts.createSourceFile(modulePath, sourceText, ts.ScriptTarget.Latest, true);
        const componentPath = `/src/${options.path}/${core_1.strings.dasherize(options.name)}.component`;
        const relativePath = (0, find_module_1.buildRelativePath)(modulePath, componentPath);
        const componentChanges = (0, ast_utils_1.addDeclarationToModule)(source, modulePath, core_1.strings.classify(`${options.name}Component`), relativePath);
        const moduleChanges = (0, ast_utils_1.addImportToModule)(source, 'ngx-extended-pdf-viewer', core_1.strings.classify(`NgxExtendedPdfViewerModule`), 'ngx-extended-pdf-viewer');
        const recorder = host.beginUpdate(modulePath);
        for (const change of componentChanges) {
            if (change instanceof change_1.InsertChange) {
                recorder.insertLeft(change.pos, change.toAdd);
            }
        }
        for (const change of moduleChanges) {
            if (change instanceof change_1.InsertChange) {
                recorder.insertLeft(change.pos, change.toAdd);
            }
        }
        host.commitUpdate(recorder);
        return host;
    };
}
function findModule(host, generateDir, moduleExt = find_module_1.MODULE_EXT, routingModuleExt = find_module_1.ROUTING_MODULE_EXT) {
    let dir = host.getDir(`/${generateDir}`);
    let foundRoutingModule = false;
    while (dir) {
        const allMatches = dir.subfiles.filter((p) => p.endsWith(moduleExt));
        const filteredMatches = allMatches.filter((p) => !p.endsWith(routingModuleExt));
        foundRoutingModule = foundRoutingModule || allMatches.length !== filteredMatches.length;
        if (filteredMatches.length == 1) {
            return (0, core_1.join)(dir.path, filteredMatches[0]);
        }
        else if (filteredMatches.length > 1) {
            throw new Error('More than one module matches. Use the skip-import option to skip importing ' +
                'the component into the closest module or use the module option to specify a module.');
        }
        dir = dir.parent;
    }
    const errorMsg = foundRoutingModule
        ? 'Could not find a non Routing NgModule.' +
            `\nModules with suffix '${routingModuleExt}' are strictly reserved for routing.` +
            '\nUse the skip-import option to skip importing in NgModule.'
        : 'Could not find an NgModule. Use the skip-import option to skip importing in NgModule.';
    throw new Error(errorMsg);
}
exports.findModule = findModule;
//# sourceMappingURL=index.js.map