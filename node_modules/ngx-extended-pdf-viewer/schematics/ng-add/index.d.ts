import { Path } from '@angular-devkit/core';
import { Rule, Tree } from '@angular-devkit/schematics';
import * as ts from 'typescript';
import { Schema } from './schema';
/**
 * Reads file given path and returns TypeScript source file.
 */
export declare function getSourceFile(host: Tree, path: string): ts.SourceFile;
/**
 * Import and add module to specific module path.
 */
export declare function addToModule(host: Tree, modulePath: string, moduleName: string, src: string): void;
export declare function ngAdd(options: Schema): Rule;
export declare function updateAngularJsonRule(projectName: string, stable: boolean): Rule;
export declare function findModule(host: Tree, generateDir: string, moduleExt?: string, routingModuleExt?: string): Path;
