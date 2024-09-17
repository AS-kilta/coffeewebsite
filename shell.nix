{ pkgs ? import <nixpkgs> {}}:
  pkgs.mkShell {
    nativeBuildInputs = let
      env = pyPkgs : with pyPkgs; [
        fastapi
        uvicorn
        opencv4
        python-decouple
        jinja2

      ];
    in with pkgs; [
      (python311.withPackages env)
    ];
}
