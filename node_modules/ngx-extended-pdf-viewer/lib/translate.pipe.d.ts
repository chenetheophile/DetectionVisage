import { PipeTransform } from '@angular/core';
import * as i0 from "@angular/core";
export declare class TranslatePipe implements PipeTransform {
    transform(key: string, fallback: string): Promise<string>;
    translate(key: string, englishText: string): Promise<string>;
    static ɵfac: i0.ɵɵFactoryDeclaration<TranslatePipe, never>;
    static ɵpipe: i0.ɵɵPipeDeclaration<TranslatePipe, "translate">;
}
