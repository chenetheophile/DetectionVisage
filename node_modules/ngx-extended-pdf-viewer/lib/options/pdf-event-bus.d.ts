export interface IEventBus {
    _listeners: Map<string, (event: any) => void>;
    on(eventName: string, listener: (event: any) => void): any;
    off(eventName: string, listener: (event: any) => void): any;
    dispatch(eventName: string, options?: any): void;
}
