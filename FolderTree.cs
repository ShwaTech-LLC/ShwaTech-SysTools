using System;
using System.IO;
using System.Text;

namespace ShwaTech {
    public class FolderTree {
        private DirectoryInfo _root;
        private FolderTree() { }
        public FolderTree( string path ) { _root = new DirectoryInfo( path ); }
        public void Prune() {
            PruneRecursive( _root );
        }
        private void PruneRecursive( DirectoryInfo root ) {
            var subs = root.GetDirectories();
            foreach( var s in subs ) {
                PruneRecursive( s );
            }
            if( subs.Length > 0 ) {
                subs = root.GetDirectories();
            }
            if( subs.Length <= 0 ) {
                var files = root.GetFiles();
                if( files.Length <= 0 ) {
                    try {
                        Console.WriteLine( "{0}", root.FullName );
                        root.Delete();
                    } catch {
                        // Directory not empty
                    }
                }
            } else {
                // Directory not empty
            }
        }
    }
}